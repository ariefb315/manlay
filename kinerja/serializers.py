from rest_framework import serializers
from kinerja.models import Ms_Pegawai, Ms_jabatan, Ms_unit_kerja, Ms_unor, Tr_header_skp, Ms_tugas_skp

class PegawaiSerializer(serializers.ModelSerializer):
    # jabatan = serializers.SlugRelatedField(queryset=Ms_jabatan.objects.all(), slug_field='nm_jabatan')
    class Meta:
        model = Ms_Pegawai
        fields = ('id', 'nip', 'nip_pimpinan', 'nama', 'pangkat', 'id_jabatan', 'id_unker', 'id_unor')
        depth=1
        # extra_kwargs = {
        #     'id_jabatan' : {'nm_jabatan'},, 'id_unker', 'id_unor'
        #     'id_unker': {'nm_unker'},
        #     'id_unor': {'nm_unor'},
        # }

class KinerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ms_tugas_skp
        fields = ('id_header_skp','keg_tgs_jbtn', 'angka_kredit', 'qty_output', 'mutu', 'waktu', 'biaya')
        depth = 1