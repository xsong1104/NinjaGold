
class ReviewManager(models.Manager):
    def addbookreview(self, userInput, user_id):
        try:
            book = self.getbook(userInput)
            user = User.objects.get(id=user_id)
            newreview = Review.objects.create(content=userInput['content'], rating=userInput['rating'], user=user, book=book)
            return (True, new_review)
        except:
            return (False, ["There was a problem creating the review..."])

    def getbook(self, userInput,):
        try:
            book = Book.objects.get(id=userInput['bookid'])
        except:
            author = self.getauthor(form_data)
            book = Book.objects.create(title=userInput['newbook'], author=author)
        return book

    def getauthor(self, userInput,):
        try:
            author = Author.objects.get(id=userInput['authorid'])
        except:
            author = Author.objects.create(name=userInput['newauthor'])
        return author

    def getrecent(self):
        return Review.objects.all().order_by('-created_at')[:5]

    def addreview(self, userInput):
        try:
            book = Book.objects.get(id=book.id)
            user = User.objects.get(id=user.id)
            newreview = Review.objects.create(content=userInput['content'], rating=userInput['rating'], user=user, book=book)
        except:
            return (False, ["There was a problem creating the review..."])
