from ckan.common import config
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def disable_user_access():
    return toolkit.asbool(config.get('ckan.senasa_theme.disable_user_access', False))


class Senasa_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    # ITemplateHelpers
    def get_helpers(self):
        return {'senasa_theme_disable_user_access': disable_user_access }

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'senasa_theme')

    # IRoutes
    def before_map(self, routing_map):
        if disable_user_access():
            self.do_disable_user_access(routing_map)
        return routing_map


    def do_disable_user_access(self, routing_map):
        routing_map.redirect('/user/login', '/')
        routing_map.redirect('/user/generate_key/{id}', '/')
        routing_map.redirect('/user/activity/{id}/{offset}', '/')
        routing_map.redirect('/user/activity/{id}', '/')
        routing_map.redirect('/user/follow/{id}', '/')
        routing_map.redirect('/user/unfollow/{id}', '/')
        routing_map.redirect('/user/followers/{id:.*}', '/')
        routing_map.redirect('/user/delete/{id}', '/')
        routing_map.redirect('/user/register', '/')
        routing_map.redirect('/user/reset', '/')
        routing_map.redirect('/user/set_lang/{lang}', '/')
        routing_map.redirect('/user', '/')
        routing_map.redirect('/user/_logout', '/logout')
        routing_map.redirect('/user/logged_out_redirect', '/')
        routing_map.redirect('/salir', '/logout')

