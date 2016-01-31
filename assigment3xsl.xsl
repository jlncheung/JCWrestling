<?xml version="1.0" encoding="ISO-8859-1"?> 

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match = "/">
  <html>
    <head><title>Products for sale </title></head>
    <body>
      <h1> Stationary Products </h1>

      <xsl:for-each select ="products/stationary">
      <xsl:sort select = "name" />

        <h3 style = "color: blue"><xsl:value-of select = "name" /></h3>
        Price: $<xsl:value-of select= "price" /><br/>
        Description: <xsl:value-of select= "description" /><br/>

        <xsl:if test = "inventory &lt;=50">
          <span style = "color: red; font-weight: bold">Inventory: <xsl:value-of select = "inventory"/></span><br/>
        </xsl:if>
        <xsl:if test = "inventory &gt;=50">
          <span style = "color: black">Inventory: <xsl:value-of select = "inventory"/></span><br/>
        </xsl:if>

      </xsl:for-each>
    </body>
  </html>	
</xsl:template>
</xsl:stylesheet>