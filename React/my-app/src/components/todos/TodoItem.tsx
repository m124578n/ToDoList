import styled from "styled-components";


//定義Props介面，todo 需符合Todo的形狀
interface Props {
    todo: Todo;
    index: number;
    onToggleTodo: ToggleTodo;
    onDeleteTodo: DeleteTodo;
}

//定義completed的style, 定義completed回傳值會是boolean型別，如果是true則劃線， false的話none
const StyledTodo = styled.span<{ complete: boolean }>`
    text-decoration: ${(props) => (props.complete ? "line-through" : "none")};
`;

//React.FC<Props> 定義這個 FunctionComponent為Props泛型
const TodoItem: React.FC<Props> = ({
    index,
    todo,
    onToggleTodo,
    onDeleteTodo,
}) => {
    return (
        <div className="form-check border border-bottom-secondary rounded py-3m-0 d-flex justify-content-between align-items-center">
            <div>
                <input 
                    className="ms-1 me-3 form-check-input"
                    type="checkbox"
                    checked={todo.complete}
                    onClick={() => {
                        onToggleTodo && onToggleTodo(index);
                    }}
                />
                <StyledTodo className="todo" complete={todo.complete}>
                    {todo.text}
                </StyledTodo>
            </div>
            
            <button
                className="btn btn-outline-danger me-3"
                onClick={() => onDeleteTodo && onDeleteTodo(index)}
            >
                X
            </button>
        </div>
        );
};

export default TodoItem;
