
BEGIN {
    in_block = 0
}
/^##### 訳注$/ {
    print
    if (!in_block) {
        print "\\begingroup\\footnotesize\\renewcommand{\\arraystretch}{0.8}"
        in_block = 1
    }
    next
}
/^#\s/ || /^##\s/ {
    if (in_block) {
        print "\\endgroup"
        in_block = 0
    }
    print
    next
}
{
    print
}
END {
    if (in_block) {
        print "\\endgroup"
    }
}
