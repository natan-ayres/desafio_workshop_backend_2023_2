from rest_framework import routers
from .views import FilmeViewset, PessoaViewset

router = routers.DefaultRouter()
router.register(r'filme', FilmeViewset)
router.register(r'pessoa', PessoaViewset)
urlpatterns = router.urls