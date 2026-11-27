// @ts-check
/**
 * Automated Test - Mutoh2000 (https://mutoh2000.com/)
 * Black Box Testing | Environment: Production | 40 test case (TC-001 .. TC-040)
 *
 * Nama test diawali ID test case agar mudah dipetakan ke Test-Case-Mutoh2000.xlsx.
 * Tidak ada transaksi pembelian, tidak ada pengiriman pesan WhatsApp, tidak ada login.
 *
 * CATATAN: selector yang tidak bisa dipastikan (wishlist, compare) dikumpulkan di objek SEL
 * di bawah. Jika gagal karena selector, sesuaikan memakai `npx playwright codegen`.
 */
const { test, expect } = require('@playwright/test');

// ───────────────────────── Konfigurasi & selector ─────────────────────────
const SEL = {
  searchInput: 'input[name="s"]',
  productLink: 'a[href*="/product/"]',
  pagination: 'a.page-numbers, .pagination a, .woocommerce-pagination a',
  nextPage: 'a.next, a.page-numbers.next, .pagination a.next',
  prevPage: 'a.prev, a.page-numbers.prev, .pagination a.prev',
  // Tema Rehub (WooCommerce): ikon hati = wishlist, tombol "Add to compare"
  wishlistBtn: '.heartplus, .wishlistadd, [class*="wishlist"][data-post_id]',
  compareBtn: '[class*="addcompare"], a:has-text("Add to compare"), span:has-text("Add to compare")',
  compareRemove: '[class*="comparemenu"] [class*="remove"], .compare-remove, [class*="remove-compare"]',
  gallery: '.woocommerce-product-gallery img, [class*="gallery"] img',
  variationSelect: 'form.variations_form select',
  langSwitcher: '[class*="lang-switch"], [class*="language"], .gtranslate_wrapper, a[hreflang], .wpml-ls, .pll-switcher',
  whatsapp: 'a[href*="api.whatsapp.com"], a[href*="wa.me"]',
};

const NO_RESULT = /tidak ditemukan|tidak ada produk|no products|nothing found|not found|tidak ada hasil/i;
const MAX_LOAD_MS = 3500;

// ───────────────────────── Helper ─────────────────────────
/** Ambil kartu produk (nama, href, teks) tanpa bergantung pada kelas CSS tema. */
async function getProductCards(page) {
  return page.$$eval('a[href*="/product/"]', (anchors) => {
    const seen = new Set();
    const out = [];
    for (const a of anchors) {
      const href = a.href;
      if (seen.has(href)) continue;
      let node = a;
      for (let i = 0; i < 6 && node && !/Rp\s?\d/.test(node.innerText || ''); i++) node = node.parentElement;
      if (!node || !/Rp\s?\d/.test(node.innerText || '')) continue;
      const nameEl = node.querySelector('h2, h3, h4') || a;
      seen.add(href);
      out.push({ href, name: (nameEl.innerText || a.innerText || a.title || '').trim(), text: node.innerText });
    }
    return out;
  });
}

/** "Rp1.337.250 Rp799.000" -> harga terakhir (harga jual) sebagai angka. */
function parseLastPrice(text) {
  const matches = [...text.matchAll(/Rp\s?([\d.]+)/g)].map((m) => parseInt(m[1].replace(/\./g, ''), 10));
  return matches.length ? matches[matches.length - 1] : NaN;
}

/** Lacak respons HTTP 5xx dan error JavaScript selama test. */
function trackErrors(page) {
  const errors = { http5xx: [], js: [] };
  page.on('response', (r) => { if (r.status() >= 500) errors.http5xx.push(`${r.status()} ${r.url()}`); });
  page.on('pageerror', (e) => errors.js.push(e.message));
  return errors;
}

async function search(page, term) {
  await page.goto('/');
  const input = page.locator(`${SEL.searchInput}:visible`).first();
  await input.fill(term);
  await input.press('Enter');
  await page.waitForLoadState('domcontentloaded');
}

async function firstProductUrl(page) {
  await page.goto('/shop/');
  const cards = await getProductCards(page);
  expect(cards.length, 'katalog harus memiliki produk').toBeGreaterThan(0);
  return cards[0].href;
}

// ═════════════════════ 3.1 Homepage & Navigation ═════════════════════
test.describe('Homepage & Navigation', () => {
  test('TC-001 Mengakses halaman utama website', async ({ page }) => {
    const errors = trackErrors(page);
    const res = await page.goto('/');
    expect(res.status()).toBeLessThan(400);
    await expect(page).toHaveTitle(/Mutoh2000/i);
    expect(errors.http5xx).toEqual([]);
  });

  test('TC-002 Memeriksa tampilan homepage', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('img').first()).toBeVisible();                        // banner/gambar
    await expect(page.getByText('BEST DEALS')).toBeVisible();                       // seksi produk
    for (const cat of ['Brankas', 'Filing Cabinet', 'Locker', 'Rak Buku']) {        // kategori
      await expect(page.getByText(cat, { exact: false }).first()).toBeAttached();
    }
    const cards = await getProductCards(page);
    expect(cards.length).toBeGreaterThan(0);
    expect(cards[0].text).toMatch(/Rp\s?\d/);                                       // informasi harga
  });

  test('TC-003 Mengakses menu utama', async ({ page }) => {
    const menu = [
      { name: 'Tentang Kami', url: /\/tentang-kami\/?$/ },
      { name: 'Kontak', url: /\/kontak-kami\/?$/ },
      { name: 'Home', url: /mutoh2000\.com\/?$/ },
    ];
    for (const item of menu) {
      await page.goto('/');
      await page.getByRole('link', { name: item.name, exact: true }).first().click();
      await expect(page).toHaveURL(item.url);
    }
  });

  test('TC-004 Mengakses submenu', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'Produk', exact: true }).first().hover();
    const sub = page.locator('a[href*="/product-category/kursi-kantor/staff"]:visible').first();
    await sub.click();
    await expect(page).toHaveURL(/\/product-category\/kursi-kantor\/staff/);
    expect((await getProductCards(page)).length).toBeGreaterThan(0);
  });

  test('TC-005 Mengakses tautan pada header dan footer', async ({ page, request }) => {
    await page.goto('/');
    const hrefs = await page.$$eval('header a[href], footer a[href]', (as) =>
      [...new Set(as.map((a) => a.href))].filter((h) => h.startsWith('https://mutoh2000.com') && !h.includes('#')));
    expect(hrefs.length).toBeGreaterThan(0);
    const broken = [];
    for (const href of hrefs.slice(0, 40)) {
      const r = await request.get(href);
      if (r.status() >= 400) broken.push(`${r.status()} ${href}`);
    }
    expect(broken, `tautan rusak: ${broken.join(', ')}`).toEqual([]);
  });
});

// ═════════════════════ 3.2 Product Catalog ═════════════════════
test.describe('Product Catalog', () => {
  test('TC-006 Mengakses katalog produk', async ({ page }) => {
    const res = await page.goto('/shop/');
    expect(res.status()).toBeLessThan(400);  
    expect((await getProductCards(page)).length).toBeGreaterThan(0);
  });

  test('TC-007 Memeriksa informasi pada katalog', async ({ page }) => {
    await page.goto('/shop/');
    const cards = (await getProductCards(page)).slice(0, 8);
    expect(cards.length).toBeGreaterThan(0);
    for (const c of cards) {
      expect(c.name.length, `nama kosong: ${c.href}`).toBeGreaterThan(0);
      expect(parseLastPrice(c.text), `harga tidak valid: ${c.name}`).toBeGreaterThan(0);
    }
    expect(await page.locator('img[src]:visible').count()).toBeGreaterThan(0);
  });

  test('TC-008 Menggunakan pagination', async ({ page }) => {
    await page.goto('/shop/');
    const next = page.locator(SEL.nextPage).first();
    test.skip((await next.count()) === 0, 'N/A: pagination tidak tersedia pada katalog');
    const before = (await getProductCards(page))[0].href;
    await next.click();
    await expect(page).toHaveURL(/page\/2|paged=2/);
    expect((await getProductCards(page))[0].href).not.toBe(before);
    await page.locator(SEL.prevPage).first().click();
    expect((await getProductCards(page))[0].href).toBe(before);
  });
});

// ═════════════════════ 3.3 Product Search ═════════════════════
test.describe('Product Search', () => {
  test('TC-009 Pencarian dengan kata kunci yang tidak tersedia (xyz123abc)', async ({ page }) => {
    const errors = trackErrors(page);
    await search(page, 'xyz123abc');
    expect((await getProductCards(page)).length).toBe(0);
    await expect(page.locator('body')).toContainText(NO_RESULT);
    expect(errors.http5xx).toEqual([]);
  });

  test('TC-010 Pencarian dengan input kosong', async ({ page }) => {
    const errors = trackErrors(page);
    await search(page, '');
    await expect(page.locator('body')).toBeVisible();
    expect(errors.http5xx).toEqual([]);
  });

  test('TC-011 Pencarian menggunakan karakter khusus (@#$%)', async ({ page }) => {
    const errors = trackErrors(page);
    await search(page, '@#$%');
    await expect(page.locator('body')).toBeVisible();
    expect(errors.http5xx).toEqual([]);
  });

  test('TC-012 Pencarian menggunakan nama produk valid (Lemari)', async ({ page }) => {
    await search(page, 'Lemari');
    const cards = await getProductCards(page);
    expect(cards.length).toBeGreaterThan(0);
    expect(cards.some((c) => /lemari/i.test(c.name))).toBeTruthy();
  });

  test('TC-013 Pencarian menggunakan sebagian nama produk (Lem)', async ({ page }) => {
    await search(page, 'Lem');
    expect((await getProductCards(page)).length).toBeGreaterThan(0);
  });
});

// ═════════════════════ 3.4 Product Category ═════════════════════
test.describe('Product Category', () => {
  test('TC-014 Memilih kategori produk', async ({ page }) => {
    await page.goto('/');
    await page.locator('a[href$="/product-category/brankas/"]:visible').first().click();
    await expect(page).toHaveURL(/\/product-category\/brankas\/?$/);
    expect((await getProductCards(page)).length).toBeGreaterThan(0);
  });

  test('TC-015 Memilih subkategori produk', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'Produk', exact: true }).first().hover();
    await page.locator('a[href*="/product-category/lemari-pakaian/lebar-90cm"]:visible').first().click();
    await expect(page).toHaveURL(/lemari-pakaian\/lebar-90cm/);
    expect((await getProductCards(page)).length).toBeGreaterThan(0);
  });

  test('TC-016 Berpindah kategori produk', async ({ page }) => {
    await page.goto('/product-category/brankas/');
    const first = (await getProductCards(page))[0].href;
    await page.goto('/product-category/rak-buku/');
    await expect(page).toHaveURL(/rak-buku/);
    const cards = await getProductCards(page);
    expect(cards.length).toBeGreaterThan(0);
    expect(cards[0].href).not.toBe(first);
  });
});

// ═════════════════════ 3.5 Filter & Sorting ═════════════════════
// Filter & sorting memakai parameter query bawaan WooCommerce (min_price, max_price, orderby).
test.describe('Filter & Sorting', () => {
  test('TC-017 Filter harga yang tidak menghasilkan produk', async ({ page }) => {
    const errors = trackErrors(page);
    await page.goto('/shop/?min_price=1&max_price=2');
    expect((await getProductCards(page)).length).toBe(0);
    expect(errors.http5xx).toEqual([]);
  });

  test('TC-018 Filter menggunakan rentang harga valid', async ({ page }) => {
    await page.goto('/shop/?min_price=300000&max_price=1000000');
    const cards = await getProductCards(page);
    expect(cards.length).toBeGreaterThan(0);
    for (const c of cards) {
      const p = parseLastPrice(c.text);
      expect(p, c.name).toBeGreaterThanOrEqual(300000);
      expect(p, c.name).toBeLessThanOrEqual(1000000);
    }
  });

  test('TC-019 Filter menggunakan nilai batas harga', async ({ page }) => {
    await page.goto('/shop/');
    const target = (await getProductCards(page))[0];
    const price = parseLastPrice(target.text);
    await page.goto(`/shop/?min_price=${price}&max_price=${price}`);
    const hrefs = (await getProductCards(page)).map((c) => c.href);
    expect(hrefs).toContain(target.href);        // batas harga bersifat inklusif
  });

  test('TC-020 Mengurutkan harga dari terendah', async ({ page }) => {
    await page.goto('/shop/?orderby=price');
    const prices = (await getProductCards(page)).map((c) => parseLastPrice(c.text));
    expect(prices.length).toBeGreaterThan(1);
    expect(prices).toEqual([...prices].sort((a, b) => a - b));
  });

  test('TC-021 Mengurutkan harga dari tertinggi', async ({ page }) => {
    await page.goto('/shop/?orderby=price-desc');
    const prices = (await getProductCards(page)).map((c) => parseLastPrice(c.text));
    expect(prices.length).toBeGreaterThan(1);
    expect(prices).toEqual([...prices].sort((a, b) => b - a));
  });
});

// ═════════════════════ 3.6 Product Detail ═════════════════════
test.describe('Product Detail', () => {
  test('TC-022 Mengakses detail produk', async ({ page }) => {
    await page.goto('/shop/');
    const card = (await getProductCards(page))[0];
    await page.goto(card.href);
    await expect(page).toHaveURL(/\/product\//);
    await expect(page.locator('h1').first()).toBeVisible();
  });

  test('TC-023 Memeriksa kesesuaian informasi produk', async ({ page }) => {
    await page.goto('/shop/');
    const card = (await getProductCards(page))[0];
    await page.goto(card.href);
    const title = (await page.locator('h1').first().innerText()).trim();
    expect(title.toLowerCase()).toContain(card.name.toLowerCase().slice(0, 25));
    const price = parseLastPrice(card.text);
    const formatted = price.toLocaleString('id-ID');            // 799000 -> "799.000"
    await expect(page.locator('body')).toContainText(formatted);
  });

  test('TC-024 Memeriksa galeri gambar produk', async ({ page }) => {
    await page.goto(await firstProductUrl(page));
    const imgs = page.locator(SEL.gallery);
    test.skip((await imgs.count()) < 2, 'N/A: produk sampel hanya memiliki satu gambar');
    await imgs.nth(1).click({ force: true });
    await expect(imgs.first()).toBeVisible();
  });

  test('TC-025 Memilih variasi produk', async ({ page }) => {
    await page.goto(await firstProductUrl(page));
    const select = page.locator(SEL.variationSelect).first();
    test.skip((await select.count()) === 0, 'N/A: produk sampel tidak memiliki variasi');
    const options = await select.locator('option:not([value=""])').all();
    await select.selectOption({ index: 1 });
    await expect(select).not.toHaveValue('');
    expect(options.length).toBeGreaterThan(0);
  });
});

// ═════════════════════ 3.7 Wishlist ═════════════════════
test.describe('Wishlist', () => {
  test('TC-027 Menambahkan produk ke wishlist', async ({ page }) => {
    await page.goto('/');
    const btn = page.locator(SEL.wishlistBtn).first();
    await btn.scrollIntoViewIfNeeded();
    await btn.click();
    await expect(btn).toHaveClass(/alreadywish|added|active/, { timeout: 8000 });
  });

  test('TC-026 Menambahkan produk yang sama secara berulang', async ({ page }) => {
    const errors = trackErrors(page);
    await page.goto('/');
    const btn = page.locator(SEL.wishlistBtn).first();
    await btn.scrollIntoViewIfNeeded();
    await btn.click();
    await btn.click();
    await expect(page.locator('body')).toBeVisible();
    expect(errors.http5xx).toEqual([]);
    expect(errors.js).toEqual([]);
  });

  test('TC-028 Menghapus produk dari wishlist', async ({ page }) => {
    await page.goto('/');
    const btn = page.locator(SEL.wishlistBtn).first();
    await btn.scrollIntoViewIfNeeded();
    await btn.click();
    await expect(btn).toHaveClass(/alreadywish|added|active/, { timeout: 8000 });
    await btn.click();                                           // klik lagi = hapus
    await expect(btn).not.toHaveClass(/alreadywish|added|active/, { timeout: 8000 });
  });
});

// ═════════════════════ 3.8 Compare Product ═════════════════════
test.describe('Compare Product', () => {
  test('TC-029 Membuka daftar perbandingan kosong', async ({ page }) => {
    const errors = trackErrors(page);
    await page.goto('/');
    // Panel "Compare items" ada di DOM dengan Total (0) saat belum ada produk.
    await expect(page.locator('body')).toContainText(/Total\s*\(0\)/);
    expect(errors.http5xx).toEqual([]);
  });

  test('TC-030 Membandingkan dua produk', async ({ page }) => {
    await page.goto('/');
    const btns = page.locator(SEL.compareBtn);
    await btns.nth(0).scrollIntoViewIfNeeded();
    await btns.nth(0).click();
    await page.waitForTimeout(800);
    await btns.nth(1).scrollIntoViewIfNeeded();
    await btns.nth(1).click();
    await expect(page.locator('body')).toContainText(/Total\s*\(2\)/, { timeout: 8000 });
  });

  test('TC-031 Menghapus produk dari daftar perbandingan', async ({ page }) => {
    await page.goto('/');
    const btn = page.locator(SEL.compareBtn).first();
    await btn.scrollIntoViewIfNeeded();
    await btn.click();
    await expect(page.locator('body')).toContainText(/Total\s*\(1\)/, { timeout: 8000 });
    await page.locator(SEL.compareRemove).first().click({ force: true });
    await expect(page.locator('body')).toContainText(/Total\s*\(0\)/, { timeout: 8000 });
  });
});

// ═════════════════════ 3.9 Language, Company Information & Contact ═════════════════════
test.describe('Language, Company Information & Contact', () => {
  test('TC-032 Mengubah bahasa website', async ({ page }) => {
    await page.goto('/');
    const sw = page.locator(SEL.langSwitcher).first();
    test.skip((await sw.count()) === 0, 'N/A: pengganti bahasa tidak ditemukan pada website');
    await sw.click();
    // Lengkapi sesuai implementasi switcher (pilih English lalu kembali ke Indonesia).
  });

  test('TC-033 Mengakses halaman informasi perusahaan', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'Tentang Kami', exact: true }).first().click();
    await expect(page).toHaveURL(/\/tentang-kami\/?$/);
    await expect(page.locator('h1, h2').first()).toBeVisible();
  });

  test('TC-034 Mengakses halaman kontak', async ({ page }) => {
    await page.goto('/');
    // Pada website, label menu adalah "Kontak" (bukan "Kontak Kami"); URL: /kontak-kami/
    await page.locator('a[href$="/kontak-kami/"]:visible').first().click();
    await expect(page).toHaveURL(/\/kontak-kami\/?$/);
    await expect(page.locator('body')).toContainText(/Jakarta|Tangerang|Whatsapp/i);
  });

  test('TC-035 Mengakses tautan WhatsApp', async ({ page }) => {
    await page.goto('/');
    const wa = page.locator(SEL.whatsapp).first();
    await expect(wa).toBeAttached();
    const href = await wa.getAttribute('href');       // tidak diklik: tidak ada pesan terkirim
    expect(href).toMatch(/phone=628\d{8,}|wa\.me\/628\d{8,}/);
  });
});

// ═════════════════════ 3.10 Error Handling ═════════════════════
test.describe('Error Handling', () => {
  test('TC-036 Mengakses URL yang tidak tersedia', async ({ page }) => {
    const res = await page.goto('/halaman-tidak-ditemukan-xyz/');
    expect(res.status()).toBe(404);
    await expect(page.locator('body')).toContainText(/404|tidak ditemukan|not found|tidak tersedia/i);
  });
});

// ═════════════════════ 3.11 Non-Functional ═════════════════════
test.describe('Non-Functional', () => {
  const viewports = [
    { name: 'desktop', width: 1366, height: 768 },
    { name: 'tablet', width: 768, height: 1024 },
    { name: 'smartphone', width: 375, height: 667 },
  ];

  for (const vp of viewports) {
    test(`TC-037 Responsivitas (${vp.name} ${vp.width}x${vp.height})`, async ({ page }) => {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      for (const path of ['/', '/shop/']) {
        await page.goto(path);
        const overflow = await page.evaluate(
          () => document.documentElement.scrollWidth - document.documentElement.clientWidth);
        expect(overflow, `scroll horizontal pada ${path}`).toBeLessThanOrEqual(1);
        expect((await getProductCards(page)).length).toBeGreaterThan(0);
      }
    });
  }

  // TC-038: dijalankan pada setiap project browser (chromium / edge / firefox) lewat playwright.config.js
  test('TC-038 Kompatibilitas browser: navigasi, pencarian, detail produk', async ({ page, browserName }, info) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Mutoh2000/i);
    await page.getByRole('link', { name: 'Tentang Kami', exact: true }).first().click();
    await expect(page).toHaveURL(/tentang-kami/);
    await search(page, 'Lemari');
    const cards = await getProductCards(page);
    expect(cards.length).toBeGreaterThan(0);
    await page.goto(cards[0].href);
    await expect(page.locator('h1').first()).toBeVisible();
    info.annotations.push({ type: 'browser', description: `${info.project.name} (${browserName})` });
  });

  test('TC-039 Waktu pemuatan halaman rata-rata <= 3,5 detik', async ({ page }) => {
    test.setTimeout(180_000);
    const productUrl = await firstProductUrl(page);
    const targets = { Homepage: '/', Katalog: '/shop/', 'Detail Produk': productUrl };
    for (const [label, url] of Object.entries(targets)) {
      const samples = [];
      for (let i = 0; i < 3; i++) {
        await page.goto('about:blank');
        await page.goto(url, { waitUntil: 'load' });
        samples.push(await page.evaluate(() => {
          const n = performance.getEntriesByType('navigation')[0];
          return n.loadEventEnd - n.startTime;
        }));
      }
      const avg = samples.reduce((a, b) => a + b, 0) / samples.length;
      test.info().annotations.push({ type: label, description: `${avg.toFixed(0)} ms (sampel: ${samples.map((s) => s.toFixed(0)).join(', ')})` });
      expect(avg, `${label} rata-rata ${avg.toFixed(0)} ms`).toBeLessThanOrEqual(MAX_LOAD_MS);
    }
  });

  test('TC-040 Memeriksa penggunaan HTTPS', async ({ page, browserName }) => {
    const res = await page.goto('/');
    expect(page.url()).toMatch(/^https:\/\//);
    if (browserName === 'chromium') {                       // securityDetails hanya tersedia di Chromium
      const sec = await res.securityDetails();
      expect(sec, 'securityDetails tersedia').not.toBeNull();
      expect(sec.validTo * 1000, 'sertifikat belum kedaluwarsa').toBeGreaterThan(Date.now());
    }
    // http:// harus dialihkan ke https://
    await page.goto('http://mutoh2000.com/');
    expect(page.url()).toMatch(/^https:\/\//);
  });
});
