from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_beath = models.DateField(null=True,blank=True)
    biography = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='authors_phoptos/',null = True, blank = True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date = models.DateField(null=True,blank=True)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=100)
    summary = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='books_phoptos/',null=True,blank=True)

class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)


from app.models import Book, Author

author, created = Author.objects.get_or_create(first_name="Robert", last_name="Greene")

book = Book.objects.create(
    title="Hokimyatning 48 qonuni",
    author=author,
    publication_date="1998-09-01",
    isbn="9780140280197",
    genre="Psixologiya",
    summary="Hokimiyatni qo‘lga kiritish va saqlash strategiyalari haqida kitob.",
    cover_image_url="https://m.media-amazon.com/images/I/61UZS3QA1UL._AC_UF1000,1000_QL80_.jpg"
)
print(f"Kitob qo‘shildi: {book.title}")
