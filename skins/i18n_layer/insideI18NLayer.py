## Script (Python) "insideI18NLayer"
##title=helper to check if inside an i18nlayer
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
REQUEST=context.REQUEST

try:
    parent = context.aq_parent
except:
    parent = None

try: 
    if parent and getattr(parent, 'meta_type', None) == 'I18NLayer':
        return 1
except: pass

return 0
