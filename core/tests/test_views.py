from django.test import Client, TestCase
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Rodrigo',
            'email': 'rousuy@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }
        self.cliente = Client()

    
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
    

    def form_invalid(self):
        dados = {
            'nome': 'rousuy',
            'assunto': 'Meu assunto'
        }
        request =  self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)