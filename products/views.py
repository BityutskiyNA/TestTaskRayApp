from http import HTTPStatus

from asgiref.sync import sync_to_async
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from drf_spectacular.utils import extend_schema

from product_catalog import settings
from products.models import Product
from products.services import save_photos


@extend_schema(
    description="Получение списка продуктов",
    summary="Список продуктов",
    tags=["Products"],
    responses={
        200: "OK",
    },
    deprecated=False,
)
class ProductListView(LoginRequiredMixin, ListView):
    """
    Класс представления для отображения списка продуктов.
    Декораторы:
    - `LoginRequiredMixin`: Требует, чтобы пользователь был аутентифицирован для доступа.
    Атрибуты:
    - `model`: Модель для этого представления.
    """

    model = Product


@extend_schema(
    description="Получение деталей продукта",
    summary="Получение деталей продукта",
    tags=["Products"],
    request=None,
    responses={
        200: "OK",
        404: {"description": "Продукт не найден"},
    },
    deprecated=False,
)
class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Класс представления для просмотра деталей продукта.
    Подклассы:
    - `LoginRequiredMixin`: Обеспечивает, что только аутентифицированные пользователи могут видеть эту страницу.
    Атрибуты:
    - `model`: Модель, используемая для получения данных о продукте.
    Методы:
    - `get_context_data`: Получает данные контекста для использования в шаблоне представления.
    """

    model = Product

    def get_context_data(self, **kwargs):
        """
        Получает данные контекста, включая изображения продукта, и добавляет их в контекст.
        Возвращает:
        dict: Словарь данных контекста.
        """
        context_data = super().get_context_data(**kwargs)
        if settings.CACHES_ENABLED:
            key = f"images_list_{self.object.pk}"
            images_list = cache.get(key)
            if images_list is None:
                images_list = self.object.images.all()
                cache.set(key, images_list)
        else:
            images_list = self.object.images.all()
        context_data["images"] = images_list
        return context_data


@extend_schema(
    description="Создание нового продукта",
    summary="Создание нового продукта",
    tags=["Products"],
    request=None,
    responses={
        200: "OK",
        400: {"description": "Некорректные данные для создания продукта"},
    },
    deprecated=False,
)
class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Класс представления для создания нового продукта.
    Подклассы:
    - `LoginRequiredMixin`: Обеспечивает, что только аутентифицированные пользователи могут видеть эту страницу.
    Атрибуты:
    - `model`: Модель, используемая для создания нового продукта.
    - `fields`: Поля формы, отображаемые на странице создания.
    """

    model = Product
    fields = (
        "name",
        "article",
        "description",
        "description",
        "product_type",
        "price",
        "quantity",
        "images",
    )
    success_url = reverse_lazy("products:index")


@extend_schema(
    description="Обновление данных продукта",
    summary="Обновление данных продукта",
    tags=["Products"],
    request=None,
    responses={
        200: "OK",
        400: {"description": "Некорректные данные для обновления продукта"},
        404: {"description": "Продукт не найден"},
    },
    deprecated=False,
)
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс представления для обновления данных продукта.
    Подклассы:
    - `LoginRequiredMixin`: Обеспечивает, что только аутентифицированные пользователи могут видеть эту страницу.
    Атрибуты:
    - `model`: Модель, используемая для обновления данных продукта.
    - `fields`: Поля формы, отображаемые на странице обновления.
    """

    model = Product
    fields = (
        "name",
        "article",
        "description",
        "description",
        "product_type",
        "price",
        "quantity",
        "images",
    )
    success_url = reverse_lazy("products:index")


@extend_schema(
    description="Удаление продукта",
    summary="Удаление продукта",
    tags=["Products"],
    responses={
        200: "OK",  # Замените на ваш класс ответа, если это предусмотрено
        403: {"description": "Отказано в доступе"},
        404: {"description": "Продукт не найден"},
    },
    deprecated=False,
)
class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Класс представления для удаления продукта.
    Подклассы:
    - `LoginRequiredMixin`: Обеспечивает, что только аутентифицированные пользователи могут видеть эту страницу.
    - `PermissionRequiredMixin`: Обеспечивает, что пользователь имеет необходимые разрешения.
    Атрибуты:
    - `model`: Модель, используемая для удаления продукта.
    - `success_url`: URL для перенаправления после успешного удаления.
    - `permission_required`: Разрешение, необходимое для доступа к этой странице.

    """

    model = Product
    success_url = reverse_lazy("products:index")
    permission_required = "products.delite.product"


@method_decorator(csrf_exempt, name="dispatch")
@extend_schema(
    description="Обновление изображений продуктов",
    summary="Обновление изображений продуктов",
    tags=["Images"],
    responses={
        200: "OK",
    },
    deprecated=False,
)
class ImageUpdateView(View):
    """
    Класс представления для обновления изображений продуктов.
    Описание этого класса и его методов можно добавить здесь.
    Декораторы:
    - `csrf_exempt`: Исключает этот класс представления из проверки CSRF.
     Методы:
    - `get_product_names_list`: Получает список названий продуктов для обновления изображений.
    - `post`: Обработчик POST-запроса для обновления изображений продуктов.
    """

    @sync_to_async
    def get_product_names_list(self):
        return list(
            Product.objects.filter(images__link__isnull=True).values("id", "name")
        )

    async def post(self, request, *args, **kwargs):
        search_queries = await self.get_product_names_list()

        await save_photos(search_queries)
        return HttpResponse(status=HTTPStatus.OK)
