function generateModelCode(modelName, $table) {
    let modelCode = `class ${modelName}(BaseModel):\n`;

    $table.find('tr').each(function() {
        const $cells = $(this).find('td');
        let name, type, defaultDisplay, description;

        if ($cells.length >= 3) {
            name = $cells.eq(0).text();
            type = $cells.eq(1).text();
            description = $cells.eq($cells.length - 1).text();
            defaultDisplay = $cells.length === 4 ? $cells.eq(2).text() : 'N';

            let fieldType = defaultDisplay === 'N' ? `Optional[${type}]` : type;
            if (defaultDisplay === 'N') 
                fieldType += ' = None';

            modelCode += `    ${name}: ${fieldType}  # ${description}\n`;
        }
    });

    return modelCode;
}

generateModelCode("MainBzParams", $($('table')[0]))
generateModelCode("MainBzFields", $($('table')[1]))

function generateArrayFromTableColumn($table) {
    let arrayResult = [];

    $table.find('tr').each(function(index) {
        // Skip the header row
        if (index === 0) return;

        const $cells = $(this).find('td');
        if ($cells.length > 0) {
            const firstColumnText = $cells.eq(0).text();
            arrayResult.push(firstColumnText);
        }
    });

    return JSON.stringify(arrayResult);
}

generateArrayFromTableColumn($($('table')[1]))
