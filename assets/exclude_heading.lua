if FORMAT:match 'commonmark' then
    function Header(block)
        if block.attr.classes:includes('hide-header') then
            return ""
        end
        if block.attr.classes:includes('hide-slide') then
            --             print(block.content)
            --             block.content = pandoc.RawInline('markdown', '')
            return ""
        end
    end

    function Div(div)
        if div.attr.classes:includes('exclude') then
            return ""
        end
    end
end
