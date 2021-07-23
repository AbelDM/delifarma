from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Integer, Double, String, DateTime, ImageUri
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from fameza.models import Product
from spyne import Array
from spyne import ComplexModel
from spyne.model.fault import Fault
from django.db.models.deletion import ProtectedError


class Productos(ComplexModel):
    id = Integer
    name = String
    price = Double
    description = String


class SoapService(ServiceBase):
    @rpc(Double(), Double(), _returns=Double)
    def suma(ctx, a, b):
        return a + b

    @rpc(_returns=Array(Productos))
    def lis(ctx):
        listado = Product.objects.values('id', 'name', 'price', 'description')
        return listado

    @rpc(Integer, _returns=String)
    def delete(ctx, id):
        try:
            p = Product.objects.filter(id=id).delete()
            return "Eliminado Producto " + str(id)
        except ProtectedError as e:
            raise Fault(faultcode="4000", faultstring=e.args[0])


Soap_app = Application(
    [SoapService],
    tns='Django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)


def consulta():
    django_soap_app = DjangoApplication(Soap_app)
    my_soap_app = csrf_exempt(django_soap_app)
    return my_soap_app
