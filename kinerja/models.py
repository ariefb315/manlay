from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.gis.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, nama, username, password=None):
        if not username:
            raise ValueError("Users must have an username!")

        user = self.model(
            nama=nama,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, nama, username, password=None):
        user = self.create_user(
            nama=nama,
            password=password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class Ms_jabatan(models.Model):
    nm_jabatan = models.CharField(max_length=50)

    def __str__(self):
        return self.nm_jabatan

class Ms_unit_kerja(models.Model):
    nm_unker = models.CharField(max_length=50)

    def __str__(self):
        return self.nm_unker

class Ms_unor(models.Model):
    nm_unor = models.CharField(max_length=50)

    def __str__(self):
        return self.nm_unor

class Ms_Pegawai(AbstractBaseUser):
    nip             = models.CharField(max_length=30)
    nip_pimpinan    = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    username        = models.CharField(max_length=30, unique=True)
    nama            = models.CharField(max_length=75)
    pangkat         = models.CharField(max_length=7)
    id_jabatan      = models.ForeignKey(Ms_jabatan, on_delete=models.CASCADE, null=True)
    id_unker        = models.ForeignKey(Ms_unit_kerja, on_delete=models.CASCADE, null=True)
    id_unor         = models.ForeignKey(Ms_unor, on_delete=models.CASCADE, null=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nama',]

    objects = MyAccountManager

    def __str__(self):
        return self.nama

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Tr_header_skp(models.Model):
    nip_pimpinan    = models.CharField(max_length=30)
    nip_pegawai     = models.ForeignKey(Ms_Pegawai, on_delete=models.CASCADE)
    tahun           = models.DateField()
    periode_awal    = models.DateField(null=True)
    periode_akhir   = models.DateField(null=True)     


class Ms_tugas_skp(models.Model):
    id_header_skp   = models.ForeignKey(Tr_header_skp, on_delete=models.CASCADE)
    keg_tgs_jbtn    = models.CharField(max_length=100)
    angka_kredit    = models.FloatField(blank=True, null=True)
    qty_output      = models.CharField(max_length=30)
    mutu            = models.IntegerField()
    waktu           = models.CharField(max_length=30)
    biaya           = models.IntegerField(null=True)

class Absensi(models.Model):
    nip             = models.ForeignKey(Ms_Pegawai, on_delete=models.CASCADE)
    tgl             = models.DateField()
    ket             = models.CharField(max_length=200, null=True)
    jam_masuk       = models.DateTimeField(null=True)
    jam_keluar      = models.DateTimeField(null=True)
    selisih_telat   = models.FloatField(null=True)
    latitude        = models.FloatField(null=True)
    longitude       = models.FloatField(null=True)
    nm_lokasi       = models.CharField(max_length=75, null=True)
    

class Ms_tugas_harian(models.Model):
    id_absensi      = models.ForeignKey(Absensi, on_delete=models.CASCADE)
    nm_tugas_harian = models.CharField(max_length=100)
    is_approved     = models.BooleanField(default=False)
    nip_pimpinan    = models.ForeignKey(Ms_Pegawai, on_delete=models.CASCADE)   



# Create your models here.
