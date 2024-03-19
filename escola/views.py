from rest_framework import viewsets, generics
from escola.models import Aluno,Curso,Matricula
from escola.serializer import AlunoSerializer, CursoSerializer,Matriculaerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """ Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = Matriculaerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """ Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer