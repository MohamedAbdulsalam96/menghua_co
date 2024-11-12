app_name = "menghua_co"
app_title = "Menghua Co"
app_publisher = "Ecosoft"
app_description = "Menghua Co\'s ERP"
app_email = "kittiu@ecosoft.co.th"
app_license = "mit"
required_apps = ["frappe/erpnext", "kittiu/thai_tax", "kittiu/sales_billing"]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "menghua_co",
# 		"logo": "/assets/menghua_co/logo.png",
# 		"title": "Menghua Co",
# 		"route": "/menghua_co",
# 		"has_permission": "menghua_co.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/menghua_co/css/menghua_co.css"
# app_include_js = "/assets/menghua_co/js/menghua_co.js"

# include js, css files in header of web template
# web_include_css = "/assets/menghua_co/css/menghua_co.css"
# web_include_js = "/assets/menghua_co/js/menghua_co.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "menghua_co/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "menghua_co/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "menghua_co.utils.jinja_methods",
# 	"filters": "menghua_co.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "menghua_co.install.before_install"
# after_install = "menghua_co.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "menghua_co.uninstall.before_uninstall"
# after_uninstall = "menghua_co.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "menghua_co.utils.before_app_install"
# after_app_install = "menghua_co.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "menghua_co.utils.before_app_uninstall"
# after_app_uninstall = "menghua_co.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "menghua_co.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"menghua_co.tasks.all"
# 	],
# 	"daily": [
# 		"menghua_co.tasks.daily"
# 	],
# 	"hourly": [
# 		"menghua_co.tasks.hourly"
# 	],
# 	"weekly": [
# 		"menghua_co.tasks.weekly"
# 	],
# 	"monthly": [
# 		"menghua_co.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "menghua_co.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "menghua_co.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "menghua_co.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["menghua_co.utils.before_request"]
# after_request = ["menghua_co.utils.after_request"]

# Job Events
# ----------
# before_job = ["menghua_co.utils.before_job"]
# after_job = ["menghua_co.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"menghua_co.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

doctype_js = {
	"Sales Order": "public/js/sales_order.js",
    "Quotation": "public/js/quotation.js",
    "Sales Billing": "public/js/sales_billing.js",
}