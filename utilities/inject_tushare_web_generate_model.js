function generateModelCode(modelName, $table) {
    let modelCode = `class ${modelName}(BaseModel):\n`;

    $table.find('tr').each(function() {
        const $cells = $(this).find('td');
        if ($cells.length == 4) {
            const name = $cells.eq(0).text();
            const type = $cells.eq(1).text();
            const defaultDisplay = $cells.eq(2).text();
            const description = $cells.eq(3).text();

            const fieldType = defaultDisplay === 'N' ? `Optional[${type}]` : type;
            modelCode += `    ${name}: ${fieldType}  # ${description}\n`;
        }

        if ($cells.length == 3) {
            const name = $cells.eq(0).text();
            const type = $cells.eq(1).text();
            const defaultDisplay = 'N';
            const description = $cells.eq(2).text();

            const fieldType = defaultDisplay === 'N' ? `Optional[${type}]` : type;
            modelCode += `    ${name}: ${fieldType}  # ${description}\n`;
        }
    });

    return modelCode;
}

generateModelCode("MainBzParams", $($('table')[0]))
generateModelCode("MainBzFields", $($('table')[1]))