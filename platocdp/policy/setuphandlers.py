from collective.grok import gs
from platocdp.policy import MessageFactory as _

@gs.importstep(
    name=u'platocdp.policy', 
    title=_('platocdp.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('platocdp.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
