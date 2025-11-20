# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths here if your modules are outside the root directory
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Brother Printer Drivers Download'
copyright = '2025, Brother Support'
author = 'Brother Support Team'

# Full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add required Sphinx extensions if needed
extensions = []

# Enable raw HTML in RST files
raw_enabled = True

# Templates directory
templates_path = ['_templates']

# Files and directories to ignore during build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# SEO-optimized titles
html_title = "How to Download Brother Printer Drivers Easily – Complete Guide"
html_short_title = "Brother Drivers Download Guide"

# Favicon (place file in _static or root)
html_favicon = 'favicon.ico'

# Hide Source Link on pages
html_show_sourcelink = False

# Allow raw/unsafe HTML in RST
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Static files directory (uncomment if needed)
# html_static_path = ['_static']
