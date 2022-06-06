
from tour import Tour

""" Make a model of an artist""" 
class Artist:


	def __init__(self,name,lyric):
		self.name=name
		self.lyric=lyric

		

	def art(self):
		#print name of artist and their lyric
		print(f"Artist:{self.name}")
		print(f"Lyric:{self.lyric}")

	def album(self,title):
		"""print the name of the album/mixtape that 
		each lyric derives from"""
		self.title=title
		print(f"Album Title: {self.title}\n") 


	def track(self,track):
		self.track=track
		print(f"Album Track Number: {self.track}")





	


	



 
the_art=Artist('Kendrick Lamar', 'Top of the Morning,Top of the Morning, Top of the Morning')
the_art.art()
the_art.track(4)
the_art.album('Baby Keem - Melodic Blues')
show=Tour()

show.random_cities()
show.randomDate()






the_art=Artist('Benny The Butcher', 'I burn you, im like the Colonel,I got a meal with the biscuit')
the_art.art()
the_art.track(7)
the_art.album('Conway The Machine - More Steriods')

the_art=Artist('Conway The Machine', 'My mind scientifc, Im rhyming prolific')
the_art.art()
the_art.track(4)
the_art.album('Conway The Machine & The Alchemist - Lulu')

the_art=Artist('Nipsey Hussle','You aint going to get it until you see it right')
the_art.art()
the_art.track(15)
the_art.album('Nipsey Hussle - MailBox Money')

the_art=Artist('Skepta','Its not a culture, its my religion')
the_art.art()
the_art.track(9)
the_art.album('Skepta - Konnichiwa')

the_art=Artist('GhostFace Killah', 'I hand glide holding on strong hard to capture')
the_art.art()
the_art.track(4)
the_art.album('Raekwon - OB4CL...')

the_art=Artist('Roc Marciano', 'It is what it is, fuxk what it could of been')
the_art.art()
the_art.track(1)
the_art.album("Roc Marciano - Rosebudd's revenge")

the_art=Artist('Giggs', 'If we are talking the hardest,Giggs better come up in your thoughts as an artist...')
the_art.art()
the_art.track(9)
the_art.album('Giggs - Ard Bodied')

the_art=Artist('Nas', 'Through the lights, cameras and action - glamour, glitters and gold, I unfold')
the_art.art()
the_art.track(12)
the_art.album('Raekwon - OB4CL...')

