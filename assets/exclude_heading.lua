if FORMAT:match 'commonmark' then
    function Header(block)
        for _, class in ipairs(block.classes) do
            if class == 'hide-header' then
                return ""
            end
        end
    end
end
