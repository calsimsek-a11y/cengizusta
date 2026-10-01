// Galeri: görsele dokununca büyük hali açılır.
(function () {
  var kutu = document.querySelector('.lightbox');
  if (!kutu || typeof kutu.showModal !== 'function') return;
  var kaynak = kutu.querySelector('source');
  var img = kutu.querySelector('img');
  var yazi = kutu.querySelector('p');

  document.querySelectorAll('.galeri-oge').forEach(function (b) {
    b.addEventListener('click', function () {
      var ad = b.dataset.ad;
      kaynak.srcset = 'img/' + ad + '-1400.avif';
      img.src = 'img/' + ad + '-1400.webp';
      img.alt = b.querySelector('img').alt;
      yazi.textContent = b.dataset.baslik;
      kutu.showModal();
    });
  });
  kutu.querySelector('.lightbox-kapat').addEventListener('click', function () { kutu.close(); });
  kutu.addEventListener('click', function (e) { if (e.target === kutu) kutu.close(); });
})();
