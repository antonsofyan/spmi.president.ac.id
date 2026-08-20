(function () {
  'use strict';

  var header = document.querySelector('header');
  if (!header) return;

  header.innerHTML = [
    '<div class="header-container">',
    '  <div class="logo">',
    '    <img src="President_University_Logo.png" alt="Logo President University" style="height:60px; margin-right:15px;">',
    '    <div>',
    '      <h1>Quality Assurance</h1>',
    '      <small>President University</small>',
    '    </div>',
    '  </div>',
    '  <nav>',
    '    <ul>',
    '      <li><a href="index.html">Home</a></li>',
    '      <li>',
    '        <a href="#">About Us <i class="fas fa-chevron-down arrow-down"></i></a>',
    '        <ul>',
    '          <li><a href="sejarah-dpmi.html"><i class="fas fa-history"></i> DPMI History</a></li>',
    '          <li><a href="visi-misi.html"><i class="fas fa-bullseye"></i> Core Values</a></li>',
    '          <li><a href="struktur-organisasi.html"><i class="fas fa-sitemap"></i> Our Team &amp; Structure</a></li>',
    '        </ul>',
    '      </li>',
    '      <li>',
    '        <a href="#">Accreditation <i class="fas fa-chevron-down arrow-down"></i></a>',
    '        <ul>',
    '          <li><a href="akreditasi.html"><i class="fas fa-certificate"></i> Accreditation</a></li>',
    '          <li><a href="alumni.html"><i class="fas fa-user-graduate"></i> Accreditation History</a></li>',
    '        </ul>',
    '      </li>',
    '      <li>',
    '        <a href="#">SPMI <i class="fas fa-chevron-down arrow-down"></i></a>',
    '        <ul>',
    '          <li><a href="ppepp.html"><i class="fas fa-sync-alt"></i> PPEPP Cycle</a></li>',
    '          <li><a href="ami.html"><i class="fas fa-clipboard-check"></i> Audit Mutu Internal</a></li>',
    '        </ul>',
    '      </li>',
    '      <li><a href="berita.html">News</a></li>',
    '      <li><a href="internasionalisasi.html">Internationalization</a></li>',
    '    </ul>',
    '  </nav>',
    '</div>'
  ].join('');
}());
