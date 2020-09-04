module Jekyll
    class PermalinkRewriter < Generator
        safe true
        priority :highest

        def generate(site)
            site.posts.each do |item|
                item.data['permalink'] = '/hi' + item.slug + '/'
            end
        end
    end
end