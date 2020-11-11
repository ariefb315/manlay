from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ms_Pegawai, Ms_tugas_harian, Ms_jabatan, Ms_tugas_skp, Ms_unit_kerja, Ms_unor, Tr_header_skp, Absensi

class PegawaiAdmin(UserAdmin):
	list_display 		= ('nip', 'nama', 'nip_pimpinan','pangkat','id_jabatan', 'id_unker', 'id_unor', 'date_joined', 'last_login')
	search_fields 		= ('nip', 'nama', 'pangkat', 'nm_unker')
	readonly_fields 	= ('date_joined', 'last_login') #tidak bisa diubah secara manual

	filter_horizontal	= ()
	list_filter 		= ()
	fieldsets 			= ()

class Jabatan(admin.ModelAdmin):
	list_display 		= ('id', 'nm_jabatan')
	search_fields 		= ()
	readonly_fields 	= () #tidak bisa diubah secara manual

	filter_horizontal	= ()
	list_filter 		= ()
	fieldsets 			= ()

admin.site.register(Ms_Pegawai, PegawaiAdmin)
admin.site.register(Ms_jabatan, Jabatan)
admin.site.register(Ms_tugas_harian)
admin.site.register(Ms_tugas_skp)
admin.site.register(Ms_unit_kerja)
admin.site.register(Ms_unor)
admin.site.register(Absensi)
admin.site.register(Tr_header_skp)
# Register your models here.
