from django.contrib import admin
from .models import Expense, Category, Income, RecurringTransaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'limit', 'user')
    list_filter = ('user',)
    search_fields = ('name',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'category', 'amount', 'user')
    list_filter = ('category', 'date', 'user')
    search_fields = ('description', 'category')
    ordering = ('-date',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'source', 'amount', 'user')
    list_filter = ('source', 'date', 'user')
    search_fields = ('description', 'source')
    ordering = ('-date',)

@admin.register(RecurringTransaction)
class RecurringTransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'transaction_type', 'amount', 'frequency', 'next_due_date', 'user', 'is_active')
    list_filter = ('transaction_type', 'frequency', 'is_active', 'user')
    search_fields = ('description',)
