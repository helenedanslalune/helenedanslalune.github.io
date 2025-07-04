# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based GitHub Pages site for "Hélène dans la lune" - a personal blog with categorized posts. The site uses a custom post organization system with YAML metadata to control which posts appear in different sections.

## Development Commands

### Building and Serving
- `bundle exec jekyll serve` - Start development server with live reload
- `bundle exec jekyll build` - Build site to `_site/` directory
- `bundle install` - Install Ruby dependencies

### Common Tasks
- Posts are stored in `_posts/` with YAML front matter
- Images are organized in `assets/images/` by category (LNs, carnivores, cursors)
- The `_data/post_meta.yml` file controls which posts appear in different sections (menu, lists, galleries, takes)

## Architecture

### Post Organization System
The site uses a unique categorization system:
- `_data/post_meta.yml` contains arrays of post filenames organized by category
- `index.md` filters posts using the "menu" array from post_meta.yml
- Posts reference their category placement through this metadata file rather than Jekyll's built-in categories

### Key Files
- `_config.yml` - Jekyll configuration with minima theme
- `_data/post_meta.yml` - Post categorization metadata
- `index.md` - Homepage that displays filtered posts based on menu metadata
- `_posts/` - All blog posts with date-prefixed filenames (2025-06-09-*.md format)

### Theme and Styling
- Uses the minima theme as base
- Custom permalink structure set to "pretty"
- Navigation configured in `_config.yml`

## File Structure Notes
- `_site/` directory contains generated site (ignored in git)
- Assets are duplicated between `assets/` and `_site/assets/` during build
- Post images are organized by topic in subdirectories