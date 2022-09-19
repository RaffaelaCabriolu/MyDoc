LINKSDIR       = source/links
.PHONY: link
link:
  @read -p "Enter a Unique Link Name: " link_name; \
  read -p "Enter the link text the user sees: " link_text; \
  read -p "Enter the URL: " link_url; \
  read -p "Enter the .py file name (use_lower_case_and_underscore of link name): " file_name; \
  echo "The link name is: " $$link_name; \
  echo "The link text is: " $$link_text; \
  echo "The URL is: " $$link_url; \
  echo "Creating the file: " $(LINKSDIR)/$$file_name".py"; \
  echo "Enter the link in content as :xref:\`"$$link_name"\`"; \
  echo "The user will see:" $$link_text; \
  echo "Make sure you build and test the link."; \
  echo "import link\n\nen_us_user_text = \"$$link_text\" \n\n\
links.xref_links.update({\"$$link_name\": (en_us_user_text, \"$$link_url\")})" \
  > $(LINKSDIR)/$$file_name".py" \
