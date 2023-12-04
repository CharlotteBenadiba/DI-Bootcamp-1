# class Pagination:
#     def __init__(self, items=None, pageSize=10):
#         self.items = items if items else []
#         self.pageSize = int(pageSize)
#         self.currentPage = 1
#         self.totalPages = -(-len(self.items) // self.pageSize)
#         self.currentPage = 1 if self.totalPages == 0 else 1

#     def getVisibleItems(self):
#         start = (self.currentPage - 1) * self.pageSize
#         end = start + self.pageSize
#         return self.items[start:end]

#     def prevPage(self):
#         self.currentPage = max(1, self.currentPage - 1)
#         return self

#     def nextPage(self):
#         self.currentPage = min(self.totalPages, self.currentPage + 1)
#         return self

#     def firstPage(self):
#         self.currentPage = 1
#         return self

#     def lastPage(self):
#         self.currentPage = self.totalPages
#         return self

#     def goToPage(self, pageNum):
#         pageNum = int(pageNum)
#         if pageNum <= 0:
#             self.currentPage = 1
#         else:
#             self.currentPage = min(self.totalPages, pageNum)
#         return self
    
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)

# print(p.getVisibleItems()) 

# p.nextPage()
# print(p.getVisibleItems())

# p.lastPage()
# print(p.getVisibleItems())

# p.goToPage(10)
# print(p.currentPage)

