<form action="{{ route('tickets.store') }}" method="POST">
    @csrf
    <label for="device_id">Dispositivo</label>
    <select name="device_id" id="device_id">
        @foreach ($devices as $device)
            <option value="{{ $device->id }}">{{ $device->name }}</option>
        @endforeach
    </select>
    
    <label for="technician_id">Técnico</label>
    <select name="technician_id" id="technician_id">
        @foreach ($technicians as $technician)
            <option value="{{ $technician->id }}">{{ $technician->name }}</option>
        @endforeach
    </select>

    <label for="description">Descripción de la Falla</label>
    <textarea name="description" id="description"></textarea>

    <button type="submit">Crear Ticket</button>
</form>
