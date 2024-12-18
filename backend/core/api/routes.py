from apifairy import response

from core.models import Category
from core.schema import CategorySchema

from . import category_api_blueprint

Category_schema = CategorySchema(many=True)


@category_api_blueprint.route("/category", methods=["GET"])
@response(Category_schema)
def category():
    return Category.query.all()
