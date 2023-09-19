# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ficha(models.Model):
    idficha = models.AutoField(db_column='IdFicha', primary_key=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
    fechafinalizacion = models.DateField(db_column='FechaFinalizacion')  # Field name made lowercase.
    id_nombreprograma = models.ForeignKey('NombrePrograma', models.DO_NOTHING, db_column='Id_NombrePrograma')  # Field name made lowercase.
    id_nivelformacion = models.ForeignKey('NivelFormacion', models.DO_NOTHING, db_column='Id_NivelFormacion')  # Field name made lowercase.
    id_jornada = models.ForeignKey('Jornada', models.DO_NOTHING, db_column='Id_Jornada')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ficha'


class Formulario(models.Model):
    idformulario = models.IntegerField(db_column='IdFormulario', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    id_tematica = models.ForeignKey('Tematica', models.DO_NOTHING, db_column='Id_Tematica')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formulario'


class Instructores(models.Model):
    idinstructor = models.IntegerField(db_column='IdInstructor', primary_key=True)  # Field name made lowercase.
    nombresinstructor = models.CharField(db_column='NombresInstructor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instructores'


class Jornada(models.Model):
    idjornada = models.AutoField(db_column='IdJornada', primary_key=True)  # Field name made lowercase.
    nombrejornada = models.CharField(db_column='NombreJornada', unique=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jornada'


class NivelFormacion(models.Model):
    idnivelformacion = models.IntegerField(db_column='IdNivelFormacion', primary_key=True)  # Field name made lowercase.
    nombrenivelformacion = models.CharField(db_column='NombreNivelFormacion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nivel_formacion'


class NombrePrograma(models.Model):
    idnombreprograma = models.IntegerField(db_column='IdNombrePrograma', primary_key=True)  # Field name made lowercase.
    nombreprograma = models.CharField(db_column='NombrePrograma', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nombre_programa'


class PreguntaOpciones(models.Model):
    idpreguntaopciones = models.IntegerField(db_column='IdPreguntaOpciones', primary_key=True)  # Field name made lowercase.
    opcion = models.CharField(db_column='Opcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_pregunta = models.ForeignKey('Preguntas', models.DO_NOTHING, db_column='Id_Pregunta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pregunta_opciones'


class Preguntas(models.Model):
    idpregunta = models.IntegerField(db_column='IdPregunta', primary_key=True)  # Field name made lowercase.
    enunciado = models.CharField(db_column='Enunciado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_tipopregunta = models.ForeignKey('TipoPregunta', models.DO_NOTHING, db_column='Id_TipoPregunta')  # Field name made lowercase.
    id_formulario = models.ForeignKey(Formulario, models.DO_NOTHING, db_column='Id_Formulario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preguntas'


class ProgramacionFicha(models.Model):
    idprogramacionficha = models.IntegerField(db_column='IdProgramacionFicha', primary_key=True)  # Field name made lowercase.
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='Id_Ficha')  # Field name made lowercase.
    id_instructor = models.ForeignKey(Instructores, models.DO_NOTHING, db_column='Id_Instructor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programacion_ficha'


class Respuestas(models.Model):
    idrespuesta = models.IntegerField(db_column='IdRespuesta', primary_key=True)  # Field name made lowercase.
    respuesta = models.TextField(db_column='Respuesta', blank=True, null=True)  # Field name made lowercase.
    id_resultado = models.ForeignKey('Resultados', models.DO_NOTHING, db_column='Id_Resultado')  # Field name made lowercase.
    id_pregunta = models.ForeignKey(Preguntas, models.DO_NOTHING, db_column='Id_Pregunta')  # Field name made lowercase.
    id_instructor = models.ForeignKey(Instructores, models.DO_NOTHING, db_column='Id_Instructor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'respuestas'


class Resultados(models.Model):
    idresultado = models.IntegerField(db_column='IdResultado', primary_key=True)  # Field name made lowercase.
    id_formulario = models.ForeignKey(Formulario, models.DO_NOTHING, db_column='Id_Formulario')  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultados'


class Rol(models.Model):
    idrol = models.IntegerField(db_column='IdRol', primary_key=True)  # Field name made lowercase.
    nombrerol = models.CharField(db_column='NombreRol', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'


class Tematica(models.Model):
    idtematica = models.IntegerField(db_column='IdTematica', primary_key=True)  # Field name made lowercase.
    nombretematica = models.CharField(db_column='NombreTematica', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tematica'


class TipoDocumento(models.Model):
    idtipodocumento = models.IntegerField(db_column='IdTipoDocumento', primary_key=True)  # Field name made lowercase.
    nombretipodoc = models.CharField(db_column='NombreTipoDoc', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoPregunta(models.Model):
    idtipopregunta = models.IntegerField(db_column='IdTipoPregunta', primary_key=True)  # Field name made lowercase.
    nombretipopregunta = models.CharField(db_column='NombreTipoPregunta', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_pregunta'


class Usuarios(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    id_tipodocumento = models.ForeignKey(TipoDocumento, models.DO_NOTHING, db_column='Id_TipoDocumento')  # Field name made lowercase.
    documento = models.CharField(db_column='Documento', unique=True, max_length=10)  # Field name made lowercase.
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Id_Rol')  # Field name made lowercase.
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='Id_Ficha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'
