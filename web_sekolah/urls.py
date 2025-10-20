from django.contrib import admin
from django.urls import path, include
from sekolah.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('kelas/', view_kelas, name='lihat_kelas'),
    path('tambah-kelas/', tambah_kelas, name='tambah_kelas'), 
    path('hapus-kelas/<uuid:id>/', hapus_kelas, name='hapus_kelas'),
    path('edit-kelas/<uuid:id>/', edit_kelas, name='edit_kelas'),
    path('kelas/<uuid:id>/', murid_kelas, name='murid_kelas'),
    # Data Siswa URLs
    path('add-siswa/', add_siswa, name='add_siswa'),
    path('tabel-data-siswa/', view_dataSiswa, name='tabel_data_siswa'),
    path('edit-data-siswa/<str:nis_tb_dataSiswa>/', edit_dataSiswa, name='edit_data_siswa'),
    path('hapus-data-siswa/<uuid:id>/', hapus_dataSiswa, name='hapus_data_siswa'),
    # Perkembangan URLs
    path('data-siswa/<str:nis>/', tampilkan_siswa, name='tampilkan_siswa'),
    path('edit-perkembangan-siswa/<uuid:id>/', edit_perkembangan, name='edit_perkembangan'),
    path('hapus-perkembangan-siswa/<uuid:id>/', hapus_perkembangan, name='hapus_perkembangan'),
    # Kegiatan URLs
    path('tambah-kegiatan/', tambah_kegiatan, name='tambah_kegiatan'),
    path('tabel-kegiatan/', tabel_kegiatan, name='tabel_kegiatan'),
    path('detail/<uuid:id>/', detail_kegiatan, name='detail_kegiatan'),
    path('edit-kegiatan/<uuid:id>/', edit_kegiatan, name='edit_kegiatan'),
    path('hapus-kegiatan/<uuid:id>/', hapus_kegiatan, name='hapus_kegiatan'),
    # Mata Pelajaran URLs
    path('tambah-guru/', tambah_guru, name='tambah_guru'),
    path('hapus-guru/<uuid:id>/', hapus_guru, name='hapus_guru'),
    # Pelajaran URLs
    path('tambah-pelajaran/', tambah_mata_pelajaran, name='tambah_mata_pelajaran'),
    path('hapus-pelajaran/<uuid:id>/', hapus_pelajaran, name='hapus_pelajaran'),
    # Jadwal Pelajaran URLs
    path('tambah-jadwal-pelajaran/', tambah_jadwal, name='tambah_jadwal_pelajaran'),
    path('tabel-jadwal-pelajaran/', list_jadwal, name='tabel_pelajaran'),
    path('jadwal/edit/<int:jadwal_id>/', edit_jadwal, name='edit_jadwal'),
    path('hapus-jadwal/<int:jadwal_id>', hapus_jadwal, name='hapus_jadwal'),

    # Halamaban Web Umum
    path('', include('habibAlby.urls')),
    path('', include('login.urls')),
        
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)