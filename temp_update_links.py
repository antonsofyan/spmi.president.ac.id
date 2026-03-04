import re

html_file = r'c:\Users\hp\Desktop\Kerjaan dashbaord\repo github\spmi.president.ac.id\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# mapping of Prodi to new Laporan AMI link
map_links = {
    'Akuntansi': 'https://drive.google.com/file/d/1arqTQXx4f3b2Z5qCjwR0YnIcdNUJsGVb/view?usp=drive_link',
    'Aktuaria': 'https://drive.google.com/file/d/1sejud8eLmgOFnQdotLamSCCdNBBGgzip/view?usp=drive_link',
    'Agribisnis': 'https://drive.google.com/file/d/1flypMJex1l2b6CIC44rGSGmCL60vqWF5/view?usp=drive_link',
    'Manajemen': 'https://drive.google.com/file/d/15REPTf8l829YTIk7J8xGU8M0QFBVTMtd/view?usp=drive_link',
    'Magister Manajemen Teknologi': 'https://drive.google.com/file/d/1XI9X8bxghsVcgL4kBjvPhwFgc6rWTLjS/view?usp=drive_link',
    'Administrasi Bisnis': 'https://drive.google.com/file/d/1kSKmSVX9wtBqOAhuILloiHmQHsTWxKr8/view?usp=drive_link',
    'Sistem Informasi': 'https://drive.google.com/file/d/1LzasfBvakYdDyivF-aetqGG9200ZugBA/view?usp=drive_link',
    'Informatika': 'https://drive.google.com/file/d/1TjM8GXuDaY3iP3k2pw2ERRI-_P_glwli/view?usp=drive_link',
    'Magister Informatika': 'https://drive.google.com/file/d/1HeR-k6F4IP5MDY6c2PSSOZF1uvD-BXf4/view?usp=drive_link',
    'Teknik Elektro': 'https://drive.google.com/file/d/1fWozq9Z-RgX6IlLkngVu1FwiDPEpcSis/view?usp=drive_link',
    'Teknik Mesin': 'https://drive.google.com/file/d/1RbzyOoUUnNdv5vot7_xYV-xsE5tC6KPW/view?usp=drive_link',
    'Teknik Lingkungan': 'https://drive.google.com/file/d/168F2LOoigqYqt4tJeRbKqBP69HAeP3rX/view?usp=drive_link',
    'Teknik Sipil': 'https://drive.google.com/file/d/1eq297okLBSwTj_rOc3q0o109f_hgAzGA/view?usp=drive_link',
    'Teknik Industri': 'https://drive.google.com/file/d/1qTT07fP5jPFDpw3278v5SW9GQVG_4eKl/view?usp=drive_link',
    'Ilmu Komunikasi': 'https://drive.google.com/file/d/1O79BzttA6hGVI6czN__G8XJ_mjzjTJnz/view?usp=drive_link',
    'Hubungan Internasional': 'https://drive.google.com/file/d/1HDHY458Aio8CwrWYkkJNQLDJhaKmysuZ/view?usp=drive_link',
    'PGSD': 'https://drive.google.com/file/d/1VdrIpUeq611OmjfCV4V-UHX93IArjcqy/view?usp=drive_link',
    'Hukum': 'https://drive.google.com/file/d/1fVz7sQLeShSnQF3BVqN7t8V7l9V39Eu8/view?usp=drive_link',
    'Magister Hukum': 'https://drive.google.com/file/d/1lTe-V0kzPseGGeCd25WDrUM7P6FLbVNE/view?usp=drive_link',
    'Arsitektur': 'https://drive.google.com/file/d/1gkVj7Qwgi6qLW24PfU4mBp68DH8P2Lnv/view?usp=drive_link',
    'Desain Interior': 'https://drive.google.com/file/d/1Mn0eO_rMOzhuJSWCTBICa3GSnEU9QmPp/view?usp=drive_link',
    'Desain Komunikasi Visual': 'https://drive.google.com/file/d/1omDJhPwnmfGEkD8aC1F7yNDv3q8Yp_rR/view?usp=drive_link',
    'Profesi Dokter': 'https://drive.google.com/file/d/1A79FD70KULc2SCa51YXG0XVDs9rGO3Y4/view?usp=drive_link',
    'Kedokteran': 'https://drive.google.com/file/d/1A79FD70KULc2SCa51YXG0XVDs9rGO3Y4/view?usp=drive_link',
}

def replacer(match):
    s = match.group(0)
    prodi_match = re.search(r'<td>(.*?)</td>', s)
    if prodi_match:
        prodi = prodi_match.group(1).strip()
        if prodi in map_links:
            # specifically target the fa-file-alt link
            s = re.sub(
                r'(<a\s+href=")([^"]+)("\s*target="_blank"\s*class="prodi-link">\s*<i\s*class="fas\s*fa-file-alt")',
                r'\g<1>' + map_links[prodi] + r'\g<3>',
                s
            )
    return s

new_html = re.sub(r'<tr>.*?</tr>', replacer, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Replacement done!")
