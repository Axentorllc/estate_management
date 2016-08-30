# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "estate_management"
app_title = "Estate Management"
app_publisher = "Manqala"
app_description = "Estate Management Software"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "info@manqala.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/estate_management/css/estate_management.css"
# app_include_js = "/assets/estate_management/js/estate_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/estate_management/css/estate_management.css"
# web_include_js = "/assets/estate_management/js/estate_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "estate_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "estate_management.install.before_install"
# after_install = "estate_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "estate_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"estate_management.tasks.all"
# 	],
# 	"daily": [
# 		"estate_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"estate_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"estate_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"estate_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "estate_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "estate_management.event.get_events"
# }

