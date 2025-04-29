class Jekyll::PostReader
    def read_posts(dir)
      read_publishable(dir, "_posts", /.*\.(markdown|md)$/)
    end
    def read_drafts(dir)
      read_publishable(dir, "_drafts", /.*\.(markdown|md)$/)
    end
  end