SCHEMA = """
Tables:

Customer(CustomerId, FirstName, LastName, Country)
Invoice(InvoiceId, CustomerId, Total)
InvoiceLine(InvoiceLineId, InvoiceId, TrackId, UnitPrice)
Track(TrackId, Name, AlbumId)
Album(AlbumId, Title, ArtistId)
Artist(ArtistId, Name)
"""