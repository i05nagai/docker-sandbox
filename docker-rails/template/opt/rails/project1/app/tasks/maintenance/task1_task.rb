# frozen_string_literal: true

module Maintenance
  class Task1Task < MaintenanceTasks::Task
    def collection
      # Collection to be iterated over
      # Must be Active Record Relation or Array
      # Article.joins(:comments).select('id', 'title')
      # Article.joins(:comments)
    end

    def process(element)
      # The work to be done in a single iteration of the task.
      # This should be idempotent, as the same element may be processed more
      # than once if the task is interrupted and resumed.
      # Rails.logger.info element
      # puts element
      # puts element.class
      # puts 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    end

  end
end
