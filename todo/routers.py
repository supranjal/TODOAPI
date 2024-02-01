from rest_framework import routers

from todo.views import Todoviewset

router = routers.DefaultRouter()
router.register(r'todo', Todoviewset)