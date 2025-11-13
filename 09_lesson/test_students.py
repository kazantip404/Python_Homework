import pytest
from sqlalchemy import text
from database import SessionLocal, Student, Base, engine


@pytest.fixture
def db_session():
    """Фикстура для работы с базой данных с автоматической очисткой"""
    # Создаем таблицы перед тестом
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        yield session
    finally:
        # Очищаем таблицу после теста
        session.execute(text("DELETE FROM students"))
        session.commit()
        session.close()


class TestStudentsCRUD:

    def test_create_student(self, db_session):
        """Тест добавления студента"""
        # Arrange
        new_student = Student(name="Иван Иванов", email="ivan@mail.com")

        # Act
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)

        # Assert
        assert new_student.id is not None
        assert new_student.name == "Иван Иванов"
        assert new_student.email == "ivan@mail.com"

        # Cleanup выполняется автоматически в фикстуре

    def test_update_student(self, db_session):
        """Тест изменения студента"""
        # Arrange - создаем студента
        student = Student(name="Петр Петров", email="petr@mail.com")
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)

        original_id = student.id

        # Act - изменяем имя
        student.name = "Петр Сидоров"
        db_session.commit()
        db_session.refresh(student)

        # Assert - проверяем изменение
        assert student.name == "Петр Сидоров"
        assert student.id == original_id  # ID не должен измениться
        assert student.email == "petr@mail.com"  # Email не меняли

    def test_delete_student(self, db_session):
        """Тест удаления студента"""
        # Arrange - создаем студента
        student = Student(name="Мария Иванова", email="maria@mail.com")
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)

        student_id = student.id

        # Проверяем, что студент создан
        existing_student = db_session.get(Student, student_id)
        assert existing_student is not None

        # Act - удаляем студента
        db_session.delete(student)
        db_session.commit()

        # Assert - проверяем что удален
        deleted_student = db_session.get(Student, student_id)
        assert deleted_student is None