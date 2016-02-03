from django.shortcuts import render
import datetime
from django.utils import timezone
from .models import Word
import random

current_year = datetime.datetime.utcnow().year

WORDS = ('exercitationem', 'perferendis', 'perspiciatis', 'laborum', 'eveniet',
        'sunt', 'iure', 'nam', 'nobis', 'eum', 'cum', 'officiis', 'excepturi',
        'odio', 'consectetur', 'quasi', 'aut', 'quisquam', 'vel', 'eligendi',
        'itaque', 'non', 'odit', 'tempore', 'quaerat', 'dignissimos',
        'facilis', 'neque', 'nihil', 'expedita', 'vitae', 'vero', 'ipsum',
        'nisi', 'animi', 'cumque', 'pariatur', 'velit', 'modi', 'natus',
        'iusto', 'eaque', 'sequi', 'illo', 'sed', 'ex', 'et', 'voluptatibus',
        'tempora', 'veritatis', 'ratione', 'assumenda', 'incidunt', 'nostrum',
        'placeat', 'aliquid', 'fuga', 'provident', 'praesentium', 'rem',
        'necessitatibus', 'suscipit', 'adipisci', 'quidem', 'possimus',
        'voluptas', 'debitis', 'sint', 'accusantium', 'unde', 'sapiente',
        'voluptate', 'qui', 'aspernatur', 'laudantium', 'soluta', 'amet',
        'quo', 'aliquam', 'saepe', 'culpa', 'libero', 'ipsa', 'dicta',
        'reiciendis', 'nesciunt', 'doloribus', 'autem', 'impedit', 'minima',
        'maiores', 'repudiandae', 'ipsam', 'obcaecati', 'ullam', 'enim',
        'totam', 'delectus', 'ducimus', 'quis', 'voluptates', 'dolores',
        'molestiae', 'harum', 'dolorem', 'quia', 'voluptatem', 'molestias',
        'magni', 'distinctio', 'omnis', 'illum', 'dolorum', 'voluptatum', 'ea',
        'quas', 'quam', 'corporis', 'quae', 'blanditiis', 'atque', 'deserunt',
        'laboriosam', 'earum', 'consequuntur', 'hic', 'cupiditate',
        'quibusdam', 'accusamus', 'ut', 'rerum', 'error', 'minus', 'eius',
        'ab', 'ad', 'nemo', 'fugit', 'officia', 'at', 'in', 'id', 'quos',
        'reprehenderit', 'numquam', 'iste', 'fugiat', 'sit', 'inventore',
        'beatae', 'repellendus', 'magnam', 'recusandae', 'quod', 'explicabo',
        'doloremque', 'aperiam', 'consequatur', 'asperiores', 'commodi',
        'optio', 'dolor', 'labore', 'temporibus', 'repellat', 'veniam',
        'architecto', 'est', 'esse', 'mollitia', 'nulla', 'a', 'similique',
        'eos', 'alias', 'dolore', 'tenetur', 'deleniti', 'porro', 'facere',
        'maxime', 'corrupti')

def home(request):
	numParagraph = request.POST.get("paragraph", "")
	start = request.POST.get("start", "")
	paragraphs = []
	randomRange = random.randint(5, 10)

	if numParagraph is None or numParagraph == "":
		numParagraph = 0

	if start == "yes":
		startParagraph = create_paragraphs(request)
		paragraphs.append("Coqui ipsum dolor amet " + startParagraph[1].lower() + startParagraph[2:])
		numParagraph = int(numParagraph) - 1

	for i in range(0, int(numParagraph)):
		paragraphs.append(create_paragraphs(request))

	return render(request, 'home/home.html', {'paragraphs':paragraphs, 'current_year':current_year})

def about(request):
	return render(request, 'home/about.html', {'current_year':current_year})

def create_paragraphs(request):
	paragraphArr = []
	paragraph = ""
	
	for i in range(random.randint(4, 8)):
		paragraphArr.append(create_sentence(request))

	for sentence in paragraphArr:
		paragraph += sentence + " "

	return paragraph

def create_sentence(request):
	word = Word.objects.all()
	filler = request.POST.get("filler", "")
	sentenceArr = []
	sentence = ""
	randomRange = random.randint(8, 15)
	randomFiller = random.randint(1, len(WORDS) - 1)


	for i in range(randomRange):
		randomIndex = random.randint(0, word.count() - 1)
		randomCommas = random.randint(2, 6)

		if i == 0:
			randomWord = word[randomIndex].word
			randomWord = randomWord[0].upper() + randomWord[1:]
		elif i == randomCommas:
			randomWord = word[randomIndex].word + ", "
		elif i%3 == 0:
			if filler == "yes":
				randomWord = WORDS[randomFiller]
			else:	
				randomWord = word[randomIndex].word	
		else:
			randomWord = word[randomIndex].word

		sentenceArr.append(randomWord)

	for word in sentenceArr:
		sentence += " " + word

	sentence += "."

	return sentence