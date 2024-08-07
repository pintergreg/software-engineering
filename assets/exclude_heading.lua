if FORMAT:match 'commonmark' then
    function Header(block)
        if block.attr.classes:includes('exclude-header') then
            return ""
        end
    end

    function Div(div)
        if div.attr.classes:includes('exclude') then
            return ""
        end
    end
end
