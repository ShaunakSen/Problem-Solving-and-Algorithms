from bs4 import BeautifulSoup

xml_data = """
<named-query name="sdfsdfsdf">
        <query>
            ---Query here...--
        </query>
</named-query>

<named-query name="xkjlias">
        <query>
          ---Query here...--
        </query>
</named-query>
"""

BeautifulSoup(markup, "lxml-xml")