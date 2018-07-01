from django.template import Library, Node

from voting import models as Ourmodel

register = Library()

class ShowVotes(Node):
	def render(self, context):
		context['num_votes'] = Ourmodel.Voting.objects.filter(candidate_id = context['candidate'].idCandidate ).count()
		return ''

def showVotes(parser, token ):
	return ShowVotes()

showVotes = register.tag(showVotes)