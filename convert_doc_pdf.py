import aspose.words as aw

doc = aw.Document("testing.docx")

saveOptions = aw.saving.PdfSaveOptions()
saveOptions.image_compression = aw.saving.PdfImageCompression.JPEG
saveOptions.jpeg_quality = 100

doc.save("pdf_result.pdf", saveOptions)
