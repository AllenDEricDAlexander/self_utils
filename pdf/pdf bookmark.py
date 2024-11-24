import PyPDF2

# 打开现有的PDF文件
with open('2324_41_13502_080202_20330174027_LW.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()

    # 将现有的内容复制到新的PDF Writer
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # 添加书签
    pdf_writer.addBookmark('Bookmark 1', 0)  # 在第一页添加书签
    pdf_writer.addBookmark('Bookmark 2', 1)  # 在第二页添加书签

    # 将书签添加到新的PDF文件中
    with open('new_file_with_bookmarks.pdf', 'wb') as new_pdf_file:
        pdf_writer.write(new_pdf_file)
