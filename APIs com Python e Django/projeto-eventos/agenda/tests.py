from django.test import TestCase, Client
from agenda.models import Evento, Categoria
from datetime import date

class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")

        # self.assertContains(response, "<th>Nome</th>")
        self.assertTemplateUsed(response, "agenda/listar_evento.html")

class TestListagemDeEventos(TestCase):
    def test_evento_hoje_e_exibido(self):
        categoria = Categoria()
        categoria.name = "backend"
        categoria.save()

        evento = Evento()
        evento.nome = "Aula de python"
        evento.categoria = categoria
        evento.local = "Rio de Janeiro"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de python")
        self.assertEqual(list(response.context["evento"]), [evento])

    def test_eventos_sem_data_sao_exibidos(self):
        categoria = Categoria()
        categoria.name = "backend"
        categoria.save()

        evento = Evento()
        evento.nome = "Aula de python"
        evento.categoria = categoria
        evento.local = "Rio de Janeiro"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de python")
        self.assertContains(response, "A definir")
        self.assertEqual(list(response.context["evento"]), [evento])