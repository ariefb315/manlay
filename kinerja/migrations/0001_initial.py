# Generated by Django 3.1.2 on 2020-10-31 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateField()),
                ('ket', models.CharField(max_length=200, null=True)),
                ('jam_masuk', models.DateTimeField(null=True)),
                ('jam_keluar', models.DateTimeField(null=True)),
                ('selisih_telat', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('nm_lokasi', models.CharField(max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ms_jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_jabatan', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ms_Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('nip', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('nama', models.CharField(max_length=75)),
                ('pangkat', models.CharField(max_length=7)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('id_jabatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_jabatan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ms_unit_kerja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_unker', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ms_unor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_unor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tr_header_skp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip_pimpinan', models.CharField(max_length=30)),
                ('tahun', models.DateField()),
                ('periode_awal', models.DateField(null=True)),
                ('periode_akhir', models.DateField(null=True)),
                ('nip_pegawai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='Ms_tugas_skp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keg_tgs_jbtn', models.CharField(max_length=100)),
                ('angka_kredit', models.FloatField(blank=True, null=True)),
                ('qty_output', models.CharField(max_length=30)),
                ('mutu', models.IntegerField()),
                ('waktu', models.CharField(max_length=30)),
                ('biaya', models.IntegerField(null=True)),
                ('id_header_skp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinerja.tr_header_skp')),
            ],
        ),
        migrations.CreateModel(
            name='Ms_tugas_harian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_tugas_harian', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('id_absensi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinerja.absensi')),
                ('nip_pimpinan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_pegawai')),
            ],
        ),
        migrations.AddField(
            model_name='ms_pegawai',
            name='id_unker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_unit_kerja'),
        ),
        migrations.AddField(
            model_name='ms_pegawai',
            name='id_unor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_unor'),
        ),
        migrations.AddField(
            model_name='ms_pegawai',
            name='nip_pimpinan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_pegawai'),
        ),
        migrations.AddField(
            model_name='absensi',
            name='nip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinerja.ms_pegawai'),
        ),
    ]
