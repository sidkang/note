# Diagram Markdown

## Node & Shape


<!-- panels:start -->

<!-- div:title-panel -->

#### Default Node

<!-- div:left-panel -->

````markdown
```mermaid
graph LR
%% use "%%" to make comment
    id1
    id2[Node with Texts]
```
````

<!-- div:right-panel -->

```mermaid
graph LR
    id1
    id2[Node with Texts]
```

<!-- div:title-panel -->

#### Node with Different Styles

<!-- div:left-panel -->

````markdown
```mermaid
graph LR
    id1(This is the text in the box)
    id2([This is the text in the box])


    id3[(Database)]







    id4((This is the text in the circle))






    id5>This is the text in the box]







    id6{This is the text in the box}






    id7{{This is the text in the box}}



    id8[/This is the text in the box/]


    id9[\This is the text in the box\]



    id10[/Christmas\]



    id11[\Go shopping/]
```
````

<!-- div:right-panel -->

```mermaid
graph LR
    id1(This is the text in the box)
    id2([This is the text in the box])
    id3[(Database)]
    id4((This is the text in the circle))
    id5>This is the text in the box]
    id6{This is the text in the box}
    id7{{This is the text in the box}}
    id8[/This is the text in the box/]
    id9[\This is the text in the box\]
    id10[/Christmas\]
    id11[\Go shopping/]
```

<!-- div:title-panel -->

#### Links

<!-- div:left-panel -->

````markdown
```mermaid
graph LR
    A --> B
    C --- D
    E -- This is the text --- F
    G---|This is the text|H
    I-->|text|J
    K-- text -->L
    M-.->N
    O-. text .-> P
    Q ==> R
```
````

<!-- div:right-panel -->

```mermaid
graph LR
    A --> B
    C --- D
    E -- This is the text --- F
    G---|This is the text|H
    I-->|text|J
    K-- text -->L
    M-.->N
    O-. text .-> P
    Q ==> R
```

<!-- div:title-panel -->

#### Chains of Links

<!-- div:left-panel -->

````markdown
```mermaid
graph LR
    A == text ==> B
    C -- text --> D -- text2 --> F
    G --> H & I --> J
    K & L--> M & N
```
````

<!-- div:right-panel -->

```mermaid
graph LR
    A == text ==> B
    C -- text --> D -- text2 --> F
    G --> H & I --> J
    K & L--> M & N
```

<!-- div:title-panel -->

#### Special characters that break syntax(Should be avoided)

<!-- div:left-panel -->

````markdown
```mermaid
graph LR
    id1["This is the (text) in the box"]
    A["A double quote:#quot;"] -->B["A dec char:#9829;"]
```
````

<!-- div:right-panel -->

```mermaid
graph LR
    id1["This is the (text) in the box"]
    A["A double quote:#quot;"] -->B["A dec char:#9829;"]
```

<!-- div:title-panel -->

#### Subgraph

<!-- div:left-panel -->

````markdown
subgraph title
    graph definition
end
````

<!-- div:right-panel -->

```mermaid
graph TB
    c1-->a2
    subgraph one
        a1-->a2
    end
    subgraph two
        b1-->b2
    end
    subgraph three
        c1-->c2
    end
```

<!-- div:title-panel -->

#### Interaction

<!-- div:left-panel -->

````markdown
# Function比较难，暂时没成功，触发链接的方式没问题
```mermaid
graph LR;
    A-->B;
    click A callback "Tooltip for a callback"
    click B "http://www.github.com" "This is a tooltip for a link"
```

<script>
    var callback = function(){
        alert('A callback was triggered')
    }
<script>
````

<!-- div:right-panel -->

```mermaid
graph LR;
%% this is a comment A -- text --> B{node}
    A-->B;
    click A callback "Tooltip for a callback"
    click B "http://www.github.com" "This is a tooltip for a link"
```

<!-- div:title-panel -->

#### Styling 待施工

<!-- panels:end -->
