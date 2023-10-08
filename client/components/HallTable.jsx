
export default function HallTable(hall) {
    return (
        <div>
            <h1>{hall.hall_name.replace('-', ' ').replace('/\b\w/g', c => c.toUpperCase())}</h1>
        </div>
    )
}