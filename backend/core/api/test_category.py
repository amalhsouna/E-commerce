import pytest

from core import database as db
from core.models import Category


@pytest.fixture
def app():
    """Create a Flask application instance for testing."""
    from core import create_app

    app = create_app()  # Use a configuration dedicated to testing
    with app.app_context():
        db.create_all()  # Create a temporary database for tests
        yield app
        db.drop_all()  # Drop the temporary database after tests


@pytest.fixture
def client(app):
    """Return a Flask test client."""
    return app.test_client()


def test_category_route(client, app):
    """Test if the /category route returns categories correctly."""
    with app.app_context():
        # Add test data to the database
        category1 = Category(name="Books", slug="books", is_active=True)
        category2 = Category(name="Electronics", slug="electronics", is_active=True)
        db.session.add_all([category1, category2])
        db.session.commit()

        # Call the /category route
        response = client.get("/api/category")

        # Perform assertions
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["name"] == "Books"
        assert data[1]["name"] == "Electronics"
